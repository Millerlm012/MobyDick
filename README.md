# MobyDick
Moby Dick Project for Source Allies.

#### Contents

- [Stack Overview](#1-stack-overview)
- [First Time Setup](#2-first-time-setup)
- [Additional Information and Project Run Down](#3-additional-information-and-project-run-down)

## 1. Stack Overview

This stack consists of:

- API: [Bottle](https://bottlepy.org/docs/dev/) (Python3)
- Frontend Web App: [SvelteKit](https://kit.svelte.dev/docs/introduction) (HTML, CSS, JS)
- Reverse Proxy: [NGINX](https://nginx.org/en/docs/)
- Deployment: [Docker](https://docs.docker.com/)
- Backend logic / Analysis: [Python3](https://docs.python.org/3.10/)

## 2. First Time Setup

To spin up the docker env for your first time, please follow the below directions. Please note, that you should already have cloned this repository to your local machine at this time.

1. Please ensure you have the following applications installed locally on your machine `npm >= 8.5.0`, `docker >= v20.10.22`, and `docker-compose >= 2.14.2`. You can accomplish checking to see if the application is installed and what the version is by running the following commands in a terminal:

```
npm -v
docker -v
docker-compose -v
```

If you're missing any of these, you will run into problems trying to follow the rest of these instrutions. Thus, go download and install them. I've included the links to the download pages for each application below. If you need assistance, contact Landon Miller.

- [NodeJS & NPM Download](https://nodejs.org/en/download/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

2. At this point, please use a terminal and ensure you're in the directory `MobyDick/app/srv/mobydick` in the code repository and run:

```
npm install
```

This should create a directory `node_modules` for us which is required for our front-end client.

3. To start our application stack, please use a terminal, and navigate to the `MobyDick/` directory inside the code repository and run: 

```
docker-compose up -d
```

OR in VSCode, right click `docker-compose.yml` and select `Compose Up`.

This will start our stack inside docker containers. 

NOTE: if you're running Windows or MacOS please ensure you have the Docker Engine running by starting Docker Desktop on your computer.

4. Finally, navigate to http://localhost in your web browser to view the final result :)

## 5. Running Tests

To run tests, please follow these simple steps:

1. Start the environment if it's not already running. To verify the stack is running, execute `docker-compose ps`. You should receive the below output from `docker-compose ps` if everything is working.

```
NAME                IMAGE               COMMAND                  SERVICE             CREATED             STATUS              PORTS
mobydick-api-1      mobydick-api        "python3 api.py"         api                 2 minutes ago       Up 2 minutes        8001/tcp
mobydick-app-1      mobydick-app        "docker-entrypoint.s…"   app                 2 minutes ago       Up 2 minutes        0.0.0.0:5173->5173/tcp, 0.0.0.0:24678->24678/tcp
mobydick-web-1      nginx:1.23-alpine   "/docker-entrypoint.…"   web                 2 minutes ago       Up 2 minutes        0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
```

2. After verifying that the stack is online, simply run `./run_tests` to run all available tests. If you're wanting to execute a specific test, pass `-t test_name`. An example of passing the `-t` flag is shown below.

```
# this will run the analysis test
./run_tests -t analysis
```

`-t` OPTIONS:
- analysis
- api
- client

## 4. Additional Information and Project Run Down

### Project Run Down:

My process for this project was first come up with a solution to the problem, "Create a list of the 100 most frequently occurring words with the count of occurrences for each word found in the attached text for Herman Melville's novel, Moby Dick. Ensure this top-100 list does not include any words in the provided stop words list." So the first thing I built was the `analysis/srv/analyze_moby_dick.py`.

After coming up with the solution, I definitely could've just displayed the finalized list via printing to the terminal or something simple like that, but I'm a Full Stack Developer, thus I wanted to show my skills and abilities as best as I can. With this in mind, I decided to build a full stack and utilize Docker just as I would do for anything else I've worked on. Please see further below to see why I chose the tech that I did.

After deciding what I was building (a full stack web app), I went ahead and built the API. After that was built, I needed to test it so, I fleshed out the reverse proxy and made sure I was able to make successful web requests to that.

Finally, once the API and NGINX was in place, I went ahead and intilized the SvelteKit app, and built out what I was envisioning for the client.

### Additional Information:

If you have questions more directly about the code, there is thourough comments throughout. Please see those first and if you have further questions, please ask!

### Why did I choose the stack that I did?

- API: [Bottle](https://bottlepy.org/docs/dev/) (Python3) - I wrote the API in Python as Python is my default language of choice. I chose to use Bottle as it's perfect for a situation where you want to spin up a REST API quickly to mock up an example. If I were to be building a larger application I would swap this out for [Flask](https://flask.palletsprojects.com/en/2.2.x/) or [Django](https://www.djangoproject.com/), both of which I've used previously in production as rest frameworks.
- Frontend Web App: [SvelteKit](https://kit.svelte.dev/docs/introduction) (HTML, CSS, JS) - I decided to utilize SvelteKit as it's amazing to work with for building web applications, and I've worked with this framework in production for prior applications as well. I optted for vanilla CSS as again, this is a quick project and doesn't need anything more serious.
- Reverse Proxy: [NGINX](https://nginx.org/en/docs/) - I decided NGINX as it's what I have the most experience with. [Apache](https://httpd.apache.org/) is another option one could utilize.
- Deployment: [Docker](https://docs.docker.com/) - I utilized docker for deployment as it's amazing for being able to build a full stack, and be able to easily share it to other developers where they can simply spin up the environment with MINIMAL to NO issues. In other words, it resolves the dreaded, "Well, it works on my machine!". With this in mind, Docker also makes deploying to production servers an easier process and sets you up future scaling!

### Why didn't I utilize a database?

- Normally when spinning up a stack I would opt to utilize [Postgres](https://www.postgresql.org/docs/) for production and [SQLite](https://www.sqlite.org/docs.html) for development. In this situation, since I was only storing the top 100 most frequent words, there really isn't much data and I didn't see a need for a true database. Simply writing to a file that the API could access is plenty.
