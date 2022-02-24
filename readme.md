# sunrise
timelapse video throughout the year

## examples
- [High Noon](https://youtu.be/zMbrEkDziwo)
- [Dawn](https://youtu.be/NFoxIiz2AVo)
- [Sunset](https://youtu.be/gmhO19kwxJ8)

## sunrise sunset tables from 
https://www.esrl.noaa.gov/gmd/grad/solcalc/table.php?lat=37.77&lon=-122.42&year=2020

https://www.esrl.noaa.gov/gmd/grad/solcalc/table.php?lat=37.77&lon=-122.42&year=2021

https://sunrise-sunset.org/us/san-francisco-ca/

https://www.timeanddate.com/sun/usa/san-francisco
tables/YYYY-MM.tsv come from timeanddate.com
highlight and copy/paste, save as tsv
then run tablesParse.js

## https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg
    "h:\ffmpeg\ffmpeg.exe" -y -r 1/5 -f concat -safe 0 -i "E:\images\imagepaths.txt" -c:v libx264 -vf "fps=25,format=yuv420p" "e:\out.mp4"

    imagespaths.txt:
    ```
    # this is a comment details https://trac.ffmpeg.org/wiki/Concatenate
    file 'E:\images\png\images__%3d.jpg'
    file 'E:\images\jpg\images__%3d.jpg'
    ```


ffmpeg -y -f concat -safe 0 -i "output.txt" -c:v libx264 -vf "fps=25,format=yuv420p" "sunrise.mp4"
ffmpeg -y -f concat -safe 0 -i "output.txt" -c:v libx264 -vf "fps=25,format=yuv420p" "sunset_after.mp4"
ffmpeg -y -f concat -safe 0 -i "output.txt" -c:v libx264 -vf "fps=25,format=yuv420p" "dusk_1yr.mp4"


re make daily movie for 2021-05-24
