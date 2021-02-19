# Tech test: MONOKU SONGS



## Context Diagram

In this short diagram, you can see the approach to implementing this API. A script was created with Docker Compose for the deployment of the application and database containers using Django and PostgresDB, additionally a "postgres_data" volume was created to persist the database information. 

![Context diagram](https://github.com/cmartinezbjmu/monoku-songs/blob/develop/docs/img/monoku_context.jpeg)

## CI PIPELINE

In this diagram, you can see a simple approach given for the Continuous Integration Pipeline. GitHub actions were used for unit test processing and code coverage. 

![CI Pipeline](https://github.com/cmartinezbjmu/monoku-songs/blob/develop/docs/img/ci_pipeline.jpeg)

## Requeriments

This API requires:

```bash
* Python versión = 3.8
* PostgreSQL version >= 12
* Install virtual environment manager 'pipenv' (https://pypi.org/project/pipenv/)
* Install docker (https://www.docker.com/get-started)
```

## Architecture and Design Choices

### Settings

This API separates Django settings to develop, staging and production environments.

All settings are located in `main.settings` as a package and this package contains four separate modules:

- **`main.settings.base`:** This file contains *default* settings that are generated with `django-admin startproject`.
- **`main.settings.develop`:** This file contains the settings for development environment.
- **`main.settings.staging`:** This file contains the settings for staging environment.
- **`main.settings.production`:** This file contains the settings production environment.

You can select which environment to run by setting the environment variable SETTINGS_MODULE. By default, `manage.py` and `main/wsgi.py` uses the` develop` settings.

The overall import schema for settings are as below:

```
└── base
    ├── development
    └── staging
    └── production
```

### PostgreSQL

This API already assumes that you will use PostgreSQL. It installs and is preconfigured to work with PostgreSQL. Check your `.env` file in the project root to further configure your setup.

### DotEnv

Due to twelve-factor app conventions, separating your configuration from application is considered to be a better practice. This API comes batteries included to use .env files in your codebase and already has a .env example file. You have to copy this file to your project root as .env for your project to run.

After copying, you better review your config file to make some changes such as secret key and database settings.



## Quick Start

### Deploy with Docker Compose

1. Clone the repository with the command "git clone https://github.com/cmartinezbjmu/monoku-songs.git"

2. Create an `.env` file.

3. Excecute this command:

   ```bash
   docker compose up
   ```

Now you can see the server running on the IP http://0.0.0.0:8000/

### Local Deploy

1. Clone the repository with the command "git clone https://github.com/cmartinezbjmu/monoku-songs.git"

2. Create an `.env` file.

3. Init your virtual environtmen 

   ```bash
   pipenv shell
   ```

4. Excecute the database migrations

   ```bash
   python manage.py migrate
   ```

5. Load database data

   ```bash
   python manage.py loaddata artist_fixtures
   python manage.py loaddata band_fixtures
   python manage.py loaddata album_fixtures
   python manage.py loaddata genre_fixtures
   python manage.py loaddata subgenre_fixtures
   python manage.py loaddata similar_band_fixtures
   python manage.py loaddata song_fixtures
   ```
   
6. Finally, init the application 

   ```bash
   python manage.py runserver
   ```



## API GraphQL

### Queries

1. Retrieve all songs:

   ```python
   query getAllSongs {
     songs {
       id
       name
       duration
       album {
         id
         name
         artist {
           id
           name
         }
         band {
           id
           name
         }
       }
       genre {
         id
         name
       }
       subgenre {
         id
         name
       }
       similarBand {
         id
         name
       }
       instrumenst
       tags
     }
   }
   ```

2. Retrieve all songs filtered by genre:

   ```python
   query getSongsFilterByGenre {
     songs(genre: "1") {
       id
       name
       duration
       album {
         id
         name
         artist {
           id
           name
         }
         band {
           id
           name
         }
       }
       genre {
         id
         name
       }    
       subgenre {
         id
         name
       }
       similarBand {
         id
         name
       }
       instrumenst
       tags
     }
   }
   ```

3. Retrieve all songs filtered by subgenre:

   ```python
   query getSongsFilterBySubgenre {
     songs(subgenre: "2") {
       id
       name
       duration
       album {
         id
         name
         artist {
           id
           name
         }
         band {
           id
           name
         }
       }
       genre {
         id
         name
       }    
       subgenre {
         id
         name
       }
       similarBand {
         id
         name
       }
       instrumenst
       tags
     }
   }
   ```

4. Retrieve all songs filtered by similar band:

   ```python
   query getSongsFilterBySimilarBand {
     songs(similarBand: "22") {
       id
       name
       duration
       album {
         id
         name
         artist {
           id
           name
         }
         band {
           id
           name
         }
       }
       genre {
         id
         name
       }    
       subgenre {
         id
         name
       }
       similarBand {
         id
         name
       }
       instrumenst
       tags
     }
   }
   ```

5. Retrieve all songs filtered by band:

   ```python
   query getSongsByBand {
     band(id: 2) {
       id
       name
       albumBand {
         songAlbum {
           name
         }
       }
     }
   }
   ```

6. Retrieve all songs filtered by artist:

   ```python
   query getSongsByArtist {
     artist(id: 2) {
       id
       name
       bandArtist {
         albumBand {
           songAlbum {
             name         
           }
         }
       }
     }
   }
   ```

### Mutation

1. Create artist:

   ```python
   mutation createArtist {
     createArtist(input: {
       name: "Kurt Cobain"
     }) {
       ok
       artist {
         id
         name
       }
     }
   }
   ```