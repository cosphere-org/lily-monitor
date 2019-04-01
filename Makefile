# Makefile

include .lily/lily_assistant.makefile


.PHONY: start_monitor
start_monitor:
	source env.sh && \
	py.test -r w -s -vv lily_monitor/rendered.py
