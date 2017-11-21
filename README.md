# Introduction

The `ox_herd_example` package illustrates how to get a very simple
application setup using `ox_herd` for job scheduling.

# Demo Via Docker

To run this example, do the following:

  1. `git clone https://github.com/emin63/ox_herd_example`
	 - This will download the git repo from github.
  2. `cd ox_herd_example`
  3. `docker-compose up --build`
	 - This will build and start the docker image.
  4. Point your browser to `http://127.0.0.1:5000/login`
  5. Login with user `test_user` and enter the password printed in the
     terminal where you started docker.
	 - The `app.py` should print a random password to the screen so that
	   only you can see it to keep things secure.
  6. After you succesfully login, go to `http://127.0.0.1:5000/ox_herd/show_plugins` to see the plugins which are loaded.
	 - Notice the `example_plugins` which is loaded by the app.py file.
  7. Click on `example_plugins` to expand it and the click on `CheckWeb`.
	 - This will take you to a form to configure the plugin.
  8. Set the name field to `test_cw` and the `queue_name` to `default` and hit the `Go` button.
	 - You have now configured this plugin to run on the given cron schedule on the default `python rq` worker queue.
  9. If you now go to the `Show_Scheduled` link at `http://127.0.0.1:5000/ox_herd/show_plugins`, you should see your plugin has been schedule.
  10. Click on your scheduled `test_cw` job and click `Launch Job Copy`.
	  - This shows how you can force launching of a copy of the job outside of the regular cron schedule.
  11. Next, click the `List Tasks` link at `http://127.0.0.1:5000/ox_herd/list_tasks` and you should see an entry for your task.
