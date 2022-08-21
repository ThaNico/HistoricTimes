# HistoricTimes

HistoricTimes is a webapp that displays historic events that happened at a specific time (hour and minute).  
For example end of the WWI hostilities at 11am in 1918.  
Users are free to add historic events (with sources) and they will be displayed after being reviewed by admins.  
The app is available on [https://historic-times.herokuapp.com](https://historic-times.herokuapp.com)

![chrome_h1qSBq18zB](https://user-images.githubusercontent.com/9906385/185783895-a7d5de51-5507-4112-a951-74867f58a061.gif)

## Tech used

- Django, Materializecss, JQuery
- For production : deployment via gunicorn on heroku [cf this awesome guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

## Ideas, future development

- Web app translation + allow multiple labels for translation
- Improve events loading (load less but on a wider range)
- With that, have a "load more" button
- Upvote events (needs to be solid and that would need accounts)
- Order events by date, votes...
- If accounts then social login could be nice

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv2](https://choosealicense.com/licenses/gpl-2.0/)

## Acknowledgment

- Of course [Stackoverflow](https://stackoverflow.com)
- [developer.mozilla.org](https://developer.mozilla.org)
- [Adobe express logo maker](https://www.adobe.com/express/create/logo)
- [Make a readme](https://www.makeareadme.com)
- [Choose a license](https://choosealicense.com)

## Dev informations

### Useful commands

- Gen secret : `python -c 'import secrets; print(secrets.token_hex(100))'`
- Create reqs : `pip-chill -v > requirements.txt` (uncomment and move django)
- Reset pip packages : `pip freeze --exclude-editable | xargs pip uninstall -y`
- Reset db in dev :
  - `find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
  - `find . -path "*/migrations/*.pyc" -delete`
  - Remove sqlite or drop, then redo migrations
- Translation :
  - Create .po files : `django-admin makemessages --all`
  - Compile them : `django-admin compilemessages`
- [Production guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment#getting_your_website_ready_to_publish)
  - python manage.py check --deploy
  - https://devcenter.heroku.com/articles/python-support#supported-python-runtimes
  - heroku create historic-times --region=eu
  - git remote -v
  - git push heroku main
  - heroku run python manage.py migrate
  - heroku run python manage.py createsuperuser
