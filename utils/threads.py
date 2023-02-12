"""
Author: Leon Burghardt
Created on: 2023-02-11

This module contains the threads of the cheat and manages them whether they are enabled or disabled.

"""

from utils.config import getConfiguration
from utils.output import print_success, print_error, print_warning
from multiprocessing import Process
from src.bhop import bhop
from src.esp import esp
from src.triggerbot import triggerbot
from src.fov import fov
import psutil
import sys


class Processes:
    p_bhop:Process = None
    p_esp:Process = None
    p_fov:Process = None
    p_triggerbot:Process = None

def bhop_change_status():
    """
    This function manages the bhop process
    """

    bhop_process = Processes.p_bhop
    if bhop_process is None:
        bhop_process = Process(target=bhop)
        Processes.p_bhop = bhop_process
    
     # create a new process for bhop
    if getConfiguration('bhop+toggle') == 'True':
        bhop_process.start()
        # check if bhop started
        if bhop_process.is_alive():
            print_success("bhop started")
        else:
            print_error("bhop failed to start")
    elif getConfiguration('bhop+toggle') == 'False':
        if bhop_process.is_alive():
            bhop_process.kill()
            Processes.p_bhop = None
        print_warning("bhop is disabled")
    else:
        print_error("bhop status could not be updated: there was an error managing the bhop process")

def esp_change_status():
    """
    This function manages the esp process
    """

    esp_process = Processes.p_esp
    if esp_process is None:
        esp_process = Process(target=esp)
        Processes.p_esp = esp_process

     # create a new process for esp
    if getConfiguration('esp+toggle') == 'True':
        esp_process.start()
        # check if esp started
        if esp_process.is_alive():
            print_success("esp started")
        else:
            print_error("esp failed to start")
    elif getConfiguration('esp+toggle') == 'False':
        if esp_process.is_alive():
            esp_process.kill()
            Processes.p_esp = None
        print_warning("esp is disabled")
    else:
        print_error("esp status could not be updated: there was an error managing the esp process")

def fov_change_status():
    """
    This function manages the fov process
    """

    fov_process = Processes.p_fov
    if fov_process is None:
        fov_process = Process(target=fov)
        Processes.p_fov = fov_process


     # create a new process for fov
    if getConfiguration('fov+toggle') == 'True':
        fov_process.start()
        # check if fov started
        if fov_process.is_alive():
            print_success("fov started")
        else:
            print_error("fov failed to start")
    elif getConfiguration('fov+toggle') == 'False':
        if fov_process.is_alive():
            fov_process.kill()
            Processes.p_fov = None
        print_warning("fov is disabled")
    else:
        print_error("fov status could not be updated: there was an error managing the fov process")

def triggerbot_change_status():
    """
    This function manages the triggerbot process
    """

    triggerbot_process = Processes.p_triggerbot
    if triggerbot_process is None:
        triggerbot_process = Process(target=triggerbot)
        Processes.p_triggerbot = triggerbot_process

     # create a new process for triggerbot
    if getConfiguration('triggerbot+toggle') == 'True':
        triggerbot_process.start()
        # check if triggerbot started
        if triggerbot_process.is_alive():
            print_success("triggerbot started")
        else:
            print_error("triggerbot failed to start")
    elif getConfiguration('triggerbot+toggle') == 'False':
        if triggerbot_process.is_alive():
            triggerbot_process.kill()
            Processes.p_triggerbot = None
        print_warning("triggerbot is disabled")
    else:
        print_error("triggerbot status could not be updated: there was an error managing the triggerbot process")


def start_threads():
    """
    Starts all the threads of the cheat.
    """

    triggerbot_change_status()
    bhop_change_status()
    esp_change_status()
    fov_change_status()

