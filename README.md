# CSV and Pandas

## Howto 

There is a bash script (normalizer .. you may need to chmod +x) that
will setup the python environment (assuming python3 is available, which
should work under ubuntu, but not on osx by default. Using something like
pyenv (https://github.com/pyenv/pyenv) can help. 

The bash script will kick off a python script that makes use of pandas. 
I thought that pandas may be helpful for this type of cleanup work. 


## CSV normalization

Please write a tool that reads a CSV formatted file on `stdin` and
emits a normalized CSV formatted file on `stdout`. Normalized, in this
case, means:

* [x] The entire CSV is in the UTF-8 character set.
* [x] The Timestamp column should be formatted in ISO-8601 format.
* [x] The Timestamp column should be assumed to be in US/Pacific time;
  please convert it to US/Eastern.
* [x] All ZIP codes should be formatted as 5 digits. If there are less
  than 5 digits, assume 0 as the prefix.
* [x] All name columns should be converted to uppercase. There will be
  non-English names.
* [ ] The Address column should be passed through as is, except for
  Unicode validation. Please note there are commas in the Address
  field; your CSV parsing will need to take that into account. Commas
  will only be present inside a quoted string.
* [x] The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
  format (where MS is milliseconds); please convert them to a floating
  point seconds format.
* [x] The column "TotalDuration" is filled with garbage data. For each
  row, please replace the value of TotalDuration with the sum of
  FooDuration and BarDuration.
* [ ]  The column "Notes" is free form text input by end-users; please do
  not perform any transformations on this column. If there are invalid
  UTF-8 characters, please replace them with the Unicode Replacement
  Character.

