#!/bin/bash

ogr2ogr -f "PostgreSQL" PG:"host=db port=5432 user=postgres dbname=postgres password=mypassword" /geodata/gdoqsocio2014shapfile/ShapFile/Quartiers_sociologiques_2014.shp \
  -lco PRECISION=no -nlt PROMOTE_TO_MULTI -nln quartiers_sociologiques -overwrite

ogr2ogr -f "PostgreSQL" PG:"host=db port=5432 user=postgres dbname=postgres password=mypassword" /geodata/mtlwifi_bornes/mtlwifi_bornes.shp \
  -lco PRECISION=no -nln mtlwifi_bornes -overwrite

ogr2ogr -f "PostgreSQL" PG:"host=db port=5432 user=postgres dbname=postgres password=mypassword" /geodata/testdata/districtshape.shp \
  -lco PRECISION=no -nln testdata -overwrite