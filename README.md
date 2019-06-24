# GoogleTranslateDestroyer
Ever wanted to put something into Google Translate and pass it through every single language, just to see what you'd end up with? No? Well, we made a web page for it anyway.

## Installation
- Install [Python](https://www.python.org/) (at least version 3)

- Open a command prompt or terminal and clone the repository (obviously):
  ```
  git clone https://github.com/i3devs/GoogleTranslateDestroyer.git
  ```
  
- Alternatively, you can download a .ZIP file containing the repository's contents via the GitHub page:
 
  ![Download the repository's ZIP file](media/download_repo_zip.png)
  You can then extract this .ZIP file wherever you like.

## Starting

### Activating the virtual environment
Open a command prompt or terminal, go to the directory where you cloned or downloaded the repository and activate the virtual environment provided with it:
```
./gtransdest_venv/Scripts/activate
```

You should see the following text preceding the directory you're in:
```text
(gtransdest_venv)
```

For example:
![Virtual environment activation](media/venv_activation.png)

### Starting Django

To start Django's web server then type the following command:
- Windows:
```
py manage.py runserver
```

- Linux / macOS:
```
python3 manage.py runserver
```

![Console command on Windows Powershell](media/windows_run.png)

## Usage
After the server has been started, you can direct your web browser to [http://localhost:8000](http://localhost:8000) to see the following page:

![Webpage](media/webpage.png)

Insert some text into the first textarea that you'd like to **destroy**, choose the language in which the text is (which is also the language of the text that will be returned to you at the end), choose a number of languages in which to translate the text from 1 to 99 and click "Send".

![Example data](media/example_data.png)

Depending on the chosen number of languages the operation will take more or less time, count an average of 1.3 seconds per language.

You can check the console with which you started the application for step-by-step updates on your text as it gets translated in every language.  

![Step-by-step updates](media/updates.png)

After some time the textarea labeled "Output" will contain your text after it's been ridiculously destroyed by Google Translate.

![Destroyed text](media/destroyed_text.png)