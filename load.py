import csv
from typing import Sized
import os
import discord
from discord.ext import commands
import pymysql
import logging
import sys


def connect():
    host = "us-cdbr-east-05.cleardb.net"
    database = "heroku_489b26d0cf8f5ad"
    username = "bc2b49a64ae3ec"
    password = "1a374319"

    try:
        # DB Connection 생성
        conn = pymysql.connect(host=host,
                               user=username,
                               passwd=password,
                               db=database,
                               use_unicode=True,
                               charset='utf8')
        cursor = conn.cursor()

    except:
        logging.error("asdf")
        sys.exit(1)

    return conn, cursor


def science_data_select():
    conn, cursor = connect()
    sql = 'SELECT text, label FROM similar_science WHERE class=%s'
    cursor.execute(sql, ('science'))
    val = cursor.fetchall()

    return val


def select2tsv():
    dataset = science_data_select()

    # write TSV files
    with open('similar_science/similar_science_data.tsv', 'w', encoding='utf-8', newline='') as f:
        tw = csv.writer(f, delimiter='\t')
        tw.writerow(['text', 'label'])
        for d in dataset:
            print(d[0]+' '+d[1])
            tw.writerow([d[0], d[1]])

    return


select2tsv()
