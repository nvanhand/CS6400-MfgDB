'''
EOS M280 LPBF process monitoring platform Lucid Vision Camera automation script
N. Devol, J. Berez
'''

import time
#from arena_api.system import system
import numpy as np
from PIL import Image as PIL_Image
from kivy.event import EventDispatcher
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
#import winsound
from datetime import datetime
from threading import Thread
import os

# https://github.com/kivy/kivy/wiki/Working-with-Python-threads-inside-a-Kivy-application

class CameraWidget(BoxLayout):
    savepath = StringProperty('')

    def __init__(self, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)
    def update(self):
        pass

class Camera(EventDispatcher):
    result = StringProperty("None")
    # Keep track of all subscribers
    subscribers = set()
    def __init__(self, save_path='/', delay=0.35, secDev=True,
                 cam1Func=True, cam2Func=False, verbose=True):

        self.save_path = save_path
        self.delay = delay
        self.secDev = secDev
        self.cam1Func = cam1Func  # True for operation in layerwise triggering mode, # or False for streaming mode
        self.cam2Func = cam2Func

        cam1_dir = os.path.join(self.save_path, 'cam1')

        if not os.path.exists(cam1_dir):
            os.makedirs(cam1_dir)
        if cam2Func:
            cam2_dir = os.path.join(self.save_path, 'cam2')
            if not os.path.exists(cam2_dir):
                os.makedirs(cam2_dir)

        self.verbose = verbose
        #self.connect()
        #self.param_setup()
        #self.task = Thread(target=self.stream)
        #self.task.daemon = True

    def stop_streaming(self):
        for device in self.devices:
            device.stop_stream()

    def connect(self):
        # Connect to the device(s) (cameras)
        tries = 0
        tries_max = 6
        sleep_time_secs = 10
        self.devices = None

        while tries < tries_max:  # Wait for device for 60 seconds
            self.devices = system.create_device()
            if not self.devices:
                if self.verbose:
                    print(
                        f'Try {tries + 1} of {tries_max}: waiting for {sleep_time_secs} '
                        f'secs for a device to be connected!')
                for sec_count in range(sleep_time_secs):
                    time.sleep(1)
                    if self.verbose:
                        print(f'{sec_count + 1} seconds passed ',
                              '.' * sec_count, end='\r')
                tries += 1
            else:
                break
        else:
            raise Exception(f'No device found! Please connect a device and run '
                            f'the example again.')

        if len(self.devices) == 2:
            self.secDev = True  # There is a second device

        self.cam1 = self.devices[0]
        if self.verbose:
            print(f'Cam 1 is:\n\t{self.cam1}')

        self.nodeMapList = [self.cam1.nodemap]

        # If there is a second device, add it to the nodemap list
        if self.secDev and self.cam2Func:
            self.cam2 = self.devices[1]
            self.nodeMapList.append(self.cam2.nodemap)
            if self.verbose:
                print(f'Cam 2 is:\n\t{self.cam2}')

        # If the function of the second device is not to stream, destroy it
        if (not self.cam2Func):
            cam2 = self.devices[1]
            system.destroy_device(cam2)

    # TODO: integration of custom params ? probably only delay is necessary, but will ask
    def param_setup(self):
        def configure_camera(nodeMap, params):
            for param_name, param_value in params.items():
                nodeMap[param_name].value = param_value
        params = {
            'TriggerSelector': 'FrameStart',
            'TriggerMode': 'On',
            'TriggerSource': 'Line0',
            'TriggerActivation': 'RisingEdge',
            'TriggerDelay': self.delay,  # [sec] (0.2)
            'ExposureAuto': 'Off',
            'ExposureTime': 0.15  # [sec] (0.17 is max for PHX200S-MC)
        }

        for idx, nodeMap in enumerate(self.nodeMapList):
            configure_camera(nodeMap, params)
            nodeMap['TriggerDelay'].value = params['TriggerDelay'] * 1000000  # convert to us
            nodeMap['ExposureTime'].value = params['ExposureTime'] * 1000000  # Convert to us
            if self.verbose:
                print(f'Cam {idx+1} exposure time: {nodeMap['ExposureTime'].value*0.000001} s: ')
                print(f'Cam {idx + 1} trigger delay: {nodeMap['TriggerDelay'].value*0.000001} s')

        for device in self.devices:
            stream_nodemap = device.tl_stream_nodemap
            stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
            stream_nodemap['StreamPacketResendEnable'].value = True


    def stream(self):
        with self.cam1.start_stream() and self.cam2.start_stream():
            #Infinitely fetch and display buffer data until esc is pressed
            while True:
                try:
                    self.trigger_armed = False
                    if self.verbose:
                        print('Waiting for trigger armed')
                    while self.trigger_armed is False:
                        self.trigger_armed = bool(self.nodeMapList[0]['TriggerArmed'].value)

                    # Trigger Image
                    if self.verbose:
                        print('Waiting for Trigger')

                    # Get image (waits here until buffer is filled up with image)
                    self.buffer = self.cam1.get_buffer()  # Blocking
                    self.image_received = time.time()
                    if self.secDev and self.cam2Func:
                        self.buffer2 = self.cam2.get_buffer()

                    if self.verbose:
                        print('Triggered')
                    winsound.Beep(440, 500)
                    self.capture()

                except KeyboardInterrupt:
                    print('Keyboard interrupt')
                    self.stop_streaming()

    def capture(self):
        buffer = self.buffer
        buffer2 = self.buffer2

        png_name = 'img_' + datetime.fromtimestamp(self.image_received).strftime('%Y-%m-%dT%H-%M-%S' + '.png')

        nparray = np.asarray(buffer.data, dtype=np.uint8)
        self.lastCam1 = nparray

        self.cam1_savepath = ''
        self.cam2_savepath = ''

        # Reshape array for pillow
        nparray_reshaped = nparray.reshape((buffer.height, buffer.width))
        if self.secDev and self.cam2Func:
            nparray2 = np.asarray(buffer2.data, dtype=np.uint8)
            self.lastCam2 = nparray2
            nparray2_reshaped = nparray2.reshape((buffer2.height, buffer2.width))
            png_array2 = PIL_Image.fromarray(nparray2_reshaped)
            self.cam2_savepath = self.save_path + '/cam2/' + png_name
            png_array2.save(self.cam2_savepath)

            self.cam2.requeue_buffer(buffer2)
        else:
            self.lastCam2 = None

        # file name is img_{year}-{month}-{day}T{hour}-{minutes}-{seconds}.png
        png_array1 = PIL_Image.fromarray(nparray_reshaped)
        self.cam1_savepath = self.save_path + '/cam1/' + png_name
        png_array1.save(self.cam1_savepath)
        self.cam1.requeue_buffer(buffer)

        self.dispatch

    def return_to_default(self):
        for nodeMap in self.nodeMapList:
            stream_params = {'TriggerSelector': 'FrameStart',
                             'TriggerMode': 'Off',
                             'TriggerSource': 'Software',
                             'TriggerDelay': 0.0,
                             'ExposureAuto': 'Continuous'}
            for key, value in stream_params.items():
                nodeMap[key].value = value

            system.destroy_device(nodeMap.device)
            print('device destroyed')

