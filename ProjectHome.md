NOTE: I have begun to move this project over to bitbucket.  The latest version can now be found here:

http://bitbucket.org/wnielson/django-chronograph/



Control django-admin commands via the web.

Creating cron jobs for Django apps can be a pain, annoying and repetitive.  With _django-chronograph_ you simply create a single cron job to run every minute, point it at your site's directory and run `manage.py cron`.  Then from the admin you can add jobs.

For example, say you're using the awesome [django-mailer](http://code.google.com/p/django-mailer/) application and you'd like to have the management command `send_mail` be run every 15 minutes.  Here's how you'd do it:

![http://i41.tinypic.com/u4hm9.png](http://i41.tinypic.com/u4hm9.png)

`Params` allow for heavy customization, thanks to the _python-dateutil_ [rrule](http://labix.org/python-dateutil#head-470fa22b2db72000d7abe698a5783a46b0731b57) module.  You'll need to have [dateutil](http://labix.org/python-dateutil#head-2f49784d6b27bae60cde1cff6a535663cf87497b) installed for _django-chronograph_ to work.

`Args` allows you to pass arguments and options to the command.

You can also run any job manually from that job's admin page (see the image above, top right).

Additionally, stdout and stderr output from each job can be logged to the database and viewed from the admin.

## Requirements ##

  * [dateutil](http://labix.org/python-dateutil#head-2f49784d6b27bae60cde1cff6a535663cf87497b)
  * >= Django 1.0