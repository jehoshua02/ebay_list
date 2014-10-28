# Setup

If you don't have them installed already, you need [pip][1] and [virtualenv][2] and [virtualenvwrapper][3].

On Mac, I installed like so. Installing python through brew comes with pip. Then I use pip to install
virtualenv.

```shell
brew install python
pip install virtualenv
pip install virtualenvwrapper
```

To avoid clobbering system packages, we use virtualenv to encapsulate dependencies for this project.
Create and activate environment for project.

```shell
mkvirtualenv ebay_list
```

Activate the environment. You'll want to do this any time you want to work on this project.

```shell
workon ebay_list
```

Lastly, install dependencies. With the environment activated, it will install them within the
environment and shield the system from being clobbered. And using pip we can install dependency
versions listed in the project.

```shell
pip install -r requirements.txt
```

Every time you stop working on this project, you should deactivate virtualenv.

```shell
deactivate
```

In addition, you'll need to "undistify" the `config/ebay.yaml.dist` file and put in actual values.


[1]: https://pip.pypa.io/en/latest/installing.html
[2]: http://virtualenv.readthedocs.org/en/latest/virtualenv.html
[3]: http://virtualenvwrapper.readthedocs.org/en/latest/index.html