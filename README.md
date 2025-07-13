# rstr
`rstr` generates a cryptographically secure random ASCII string of a given length using the system's random bytes generator.

---

## Platform Support

- Currently supports **Linux-based systems only**.

---

## Tested Systems

- Debian "Bookworm"
- Android 12 (Termux)

---

## Installation

Currently, installable packages are available for Debian-based disributions only. Manual installation is possible via `make` for others.

### Install via APT (Recommended)

You can install `rstr` using the APT package manager from the official GitHub-hosted `stable` repository.

#### Step 1: Add the APT repository

- For **Termux**, run:

```bash
export TERMUX_ROOT="$HOME/../usr"
mkdir -p $TERMUX_ROOT/etc/apt/sources.list.d
echo "deb [trusted=yes arch=all] https://arijitkd.github.io/rstr/packages/pkg stable main" | tee $TERMUX_ROOT/etc/apt/sources.list.d/rstr.list
```

- For other **Debian-based distributions**, run:

```bash
echo "deb [trusted=yes arch=all] https://arijitkd.github.io/rstr/packages/apt stable main" | sudo tee /etc/apt/sources.list.d/rstr.list
```

> `trusted=yes` is used here because the repository is not signed with a GPG key.

#### Step 2: Update APT cache

- For **Termux**, run:

```bash
pkg update
```

- For other **Debian-based distributions**, run:

```bash
sudo apt update
```

#### Step 3: Install `rstr`

- For **Termux**, run:

```bash
pkg install rstr
```

- For other **Debian-based distributions**, run:

```bash
sudo apt install rstr
```

---

### Installation from Releases

If you prefer, you can manually download and install the `.deb` package from the [Releases](https://github.com/ArijitKD/rstr/releases) section of the GitHub repository.

#### Step 1: Download the `.deb` package

 - Visit: [https://github.com/ArijitKD/rstr/releases](https://github.com/ArijitKD/rstr/releases)  
 - Download the latest `.deb` file for your system.

#### Step 2: Install using `dpkg`

```bash
sudo dpkg -i <deb-package-name>
```

> Replace `<deb-package-name>` with the actual name of the downloaded package.

#### Step 3: Fix dependencies (if required)

```bash
sudo apt install -f
```

---

### Manaul installation using `make` (for non-Debian-based systems)

#### Step 1: Get `make` and `git`

Install `make` and `git` if you don't have it already. Installation procedure may vary depending on your package manager. Consult your system documentation for guidance.

#### Step 2: Clone the repository

In your preferred workspace directory, run:

```bash
git clone https://github.com/ArijitKD/rstr.git rstr-main
```

#### Step 3: Install using `make`

Run as `root`:

```bash
cd rstr-main
make install
```

#### Step 4 (optional): Uninstallation

To uninstall, assuming you are in the toplevel directory of the repository (`rstr-main` as per above), run as `root`:

```bash
make uninstall
```

---

## Help section:

```
Help for rstr (version: 1.0)

rstr: Generate a cryptographically secure random ASCII string of a given length
using the system's random bytes generator.

#1 Possible usage patterns:
  1. rstr [<string-length>] [{-u | --ucase}] [{-l | --lcase}] \
          [{-d | --digit}] [{-s | --special}]
  2. rstr {-h | --help}
  3. rstr {-v | --version}

#2 Meanings of notations used above:
  - <...>         :  A mandatory value that must not contain a space anywhere.
  - {... | ...}   :  A shorthand and full name for the same option.
  - [...]         :  Non-mandatory options.

#3 Available options:
  1. -u, --ucase :   Specify whether to include upper case ASCII characters.
  2. -l, --lcase :   Specify whether to include lower case ASCII characters.
  3. -d, --digit :   Specify whether to include ASCII digits.
  4. -s, --special : Specify whether to include special characters.
                     
#4 Points to be noted:
  - If none of the options are specified, including the length, then the
    generated string has 16 characters and may contain all of upper case,
    lower case, digit or special ASCII characters.

  - If the length is specified, but none of the other options are specified,
    then the generated string has the specified length and contains a mix of
    all three types of ASCII characters as mentioned in the previous point.

  - Irrespective of whether the length is specified or not, if at least one
    of the 4 available options from section #3 is specified, all other options
    except the one(s) specified will be excluded from the generated string.

  - Special characters include only these:
    ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/'].

```

---

## Man Page

`man` page is currently unavailable. Use `rstr --help` instead for details.

---

## Copyright and License
Copyright (c) 2025-Present Arijit Kumar Das [<arijitkdgit.official@gmail.com>](mailto:arijitkdgit.official@gmail.com)
This software is licensed under the GNU General Public License v3+.  
You may redistribute and/or modify it under the terms of the GPL.  
There is no warranty, express or implied.

For more details, see [LICENSE](./LICENSE).

---

## Contribution

Contributions and suggestions are welcome.

---

## Bug reports

Report bugs to [arijitkdgit.official@gmail.com](mailto:arijitkdgit.official@gmail.com) or create an issue in the [Issues](https://github.com/ArijitKD/rstr/issues) section.

