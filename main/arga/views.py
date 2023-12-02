import os.path
import re
import time
from pathlib import Path
from django.shortcuts import render
from pydub import AudioSegment
from .models import Audio_store
from .forms import AudioForm


def index(request):
    music = Audio_store.objects.all()
    print(music)
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            print(form)
            file = request.FILES['record']
            print(file)
            path_file_str = '//' + 'media//media' + '//' + str(file)
            file_white = path_file_str.replace(" ", "_")
            file_white = re.sub('[()]', '', file_white)
            file_white = re.sub('[,]', '', file_white)
            print(file_white)

            if Path(file_white).exists():
                os.remove(file_white)
                #time.sleep(1)
                form.save()
            else:
                form.save()


            filename = file_white
            sound = AudioSegment.from_file(filename, format="mp3")
            print(filename)
            octaves = 0.5
            new_sample_rate = int(sound.frame_rate * (0.7 ** octaves))
            pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
            pitch_sound = pitch_sound.set_frame_rate(44100)
            pitch_sound.export(filename, format="mp3")
            print(sound)

            return render(request, 'index.html', { 'form': form, 'audio_file': filename})
    else:
        form = AudioForm()

    return render(request, 'index.html', {'form': form})

