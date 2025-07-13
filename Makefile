#!/usr/bin/make
#
# File: Makefile
#
# rstr - Generate a cryptographically secure random ASCII string of a given
# length using the system's random bytes generator.
#
#
# Copyright (C) 2025-Present Arijit Kumar Das <arijitkdgit.official@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


PREFIX       ?= /usr
LIBDIR       := $(PREFIX)/lib/rstr
BINDIR       := $(PREFIX)/bin
SCRIPT_PATH  := $(BINDIR)/rstr
MAIN_SCRIPT  := $(LIBDIR)/rstr.py

.PHONY: all help install uninstall

all: help

help:
	@echo "Run as root"
	@echo "  - To install: make install"
	@echo "  - To uninstall: make uninstall"
	@echo "You can also specify PREFIX=<dir> to specify the top-level install directory."


install:
	@if [ "$$(id -u)" -ne 0 ]; then \
		echo "Please run 'make install' as root."; \
		exit 1; \
	fi

	@echo "Creating shell wrapper at: $(SCRIPT_PATH)"
	@echo '#!/bin/bash'																					>  rstr_temp
	@echo '#'																							>> rstr_temp
	@echo '# File: rstr'																				>> rstr_temp
	@echo '#'																							>> rstr_temp
	@echo '# rstr - Generate a cryptographically secure random ASCII string of a given'					>> rstr_temp
	@echo "# length using the system's random bytes generator."											>> rstr_temp
	@echo '#'																							>> rstr_temp
	@echo '# Copyright (C) 2025-Present Arijit Kumar Das <arijitkdgit.official@gmail.com>'				>> rstr_temp
	@echo '#'																							>> rstr_temp
	@echo '# License: GPLv3+'																			>> rstr_temp
	@echo '#'																							>> rstr_temp
	@echo 'exec /usr/bin/python3 $(MAIN_SCRIPT) "$$@"'													>> rstr_temp
	@install -Dm755 rstr_temp $(SCRIPT_PATH)
	@rm -f rstr_temp

	@echo "Creating directory: $(LIBDIR)"
	@install -d $(LIBDIR)

	@echo "Copying main script to: $(MAIN_SCRIPT)"
	@install -Dm644 src/rstr.py $(MAIN_SCRIPT)

	@echo "Installation successful."
	@echo "Run 'rstr -h' to read the Help section."

uninstall:
	@if [ "$$(id -u)" -ne 0 ]; then \
		echo "Please run 'make uninstall' as root."; \
		exit 1; \
	fi

	@echo "Removing shell wrapper: $(SCRIPT_PATH)"
	@rm -f $(SCRIPT_PATH)

	@echo "Removing installed files from: $(LIBDIR)"
	@rm -rf $(LIBDIR)

	@echo "Uninstallation complete."

