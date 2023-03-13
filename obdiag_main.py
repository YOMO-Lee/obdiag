#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@file: obdiag_main.py
@desc:
"""

from common.logger import logger

from obdiag_client import OBDIAGClient
from utils.parser_utils import ArgParser

CONFIG_PARSE_IGNORE_ATTR = ["start_date", "end_date"]
DEFAULT_SINCE_HOURS = 12


def pharse_config(args):
    try:
        if args.config:
            args.config(args)
    except AttributeError:
        logger.info("object has no attribute 'config' pass quick config\n")


def gather_log(args):
    try:
        if args.gather_log:
            args.gather_log(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_log' pass gather log\n")


def gather_awr(args):
    try:
        if args.gather_awr:
            args.gather_awr(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_awr' pass gather awr\n")


def gather_sysstat(args):
    try:
        if args.gather_sysstat:
            args.gather_sysstat(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_sysstat' pass gather sysstat info\n")


def gather_perf(args):
    try:
        if args.gather_perf:
            args.gather_perf(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_perf' pass gather perf info\n")


def gather_plan_monitor(args):
    try:
        if args.gather_plan_monitor:
            args.gather_plan_monitor(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_plan_monitor' pass gather ob sql plan monitor\n")


def gather_clog(args):
    try:
        if args.gather_clog:
            args.gather_clog(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_clog' pass gather clog\n")

def gather_slog(args):
    try:
        if args.gather_slog:
            args.gather_slog(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_slog' pass gather slog\n")

def gather_obproxy_log(args):
    try:
        if args.gather_obproxy_log:
            args.gather_obproxy_log(args)
    except AttributeError:
        logger.info("object has no attribute 'gather_obproxy_log' pass gather obproxy log\n")


if __name__ == '__main__':
    obdiag = OBDIAGClient().init()
    arg_parser = ArgParser(obdiag)
    obdiag_args = arg_parser.parse_argv()
    pharse_config(obdiag_args)
    gather_log(obdiag_args)
    gather_awr(obdiag_args)
    gather_sysstat(obdiag_args)
    gather_perf(obdiag_args)
    gather_plan_monitor(obdiag_args)
    gather_clog(obdiag_args)
    gather_slog(obdiag_args)
    gather_obproxy_log(obdiag_args)