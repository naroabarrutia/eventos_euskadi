from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'eventos_euskadi',         # How you named your package folder (MyLib)
  packages = ['eventos_euskadi'],   # Chose the same as "name"
  version = '1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Información y análisis de eventos culturales de Euskadi.',   # Give a short description about your library
  author = 'Mikel Madariaga & Naroa Barrutia',                   # Type in your name
  author_email = 'naroa.barrutia@alumni.mondragon.edu',      # Type in your E-Mail
  url = 'https://github.com/naroabarrutia/eventos_euskadi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/naroabarrutia/eventos_euskadi/archive/refs/tags/v_1.2.tar.gz',    # I explain this later on
  keywords = ['EVENTOS', 'EUSKADI', 'OPENDATA'], # Keywords that define your package best
  long_description=long_description,
  long_description_content_type='text/markdown',  # This is important!
  install_requires=[            # I get to this in a second
          'requests',
          'pandas',
          'seaborn',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)