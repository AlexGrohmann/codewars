#!/bin/sh

dad_years_old=$1
son_years_old=$2
double_son_age=${2}*2
age_gap=$((dad_years_old-double_son_age))

echo ${age_gap#-}

sleep 5
exit
