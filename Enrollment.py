from flask import Flask, request, render_template, redirect
from init import student_data, courses_data, time_slot_data, enrolledtable_data

def oenroll():
    return True