# -*- coding: utf-8 -*-

"""Main module."""
import csv
import re
import configparser
import argparse


parser = argparse.ArgumentParser(description='Search some data a csv')
parser.add_argument('--out', '-o', type=str,
                    help='path to save file(default: out.csv)')
parser.add_argument('--encoding', type=str,
                    help='encoding to use for csv_file(default: UTF-8)')
parser.add_argument('conf', type=str, help='config file')
parser.add_argument('csv_file', type=str, help='csv file to filter')


def finder(in_filename, out_filename, filters, encoding, csv_opt=None):
    out_file = open(out_filename, 'w+', encoding=encoding)
    csv_opt = csv_opt or {}
    writer = csv.writer(out_file, **csv_opt)
    with open(in_filename, encoding=encoding) as in_file:
        reader = csv.reader(in_file, **csv_opt)
        headers = next(reader)
        writer.writerow(headers)
        for row in reader:
            row_dict = {header: val for header, val in zip(headers, row)}
            for filter_, ftype in filters:
                if apply_filter(filter_, ftype, row_dict):
                    writer.writerow(row)
                    break
    out_file.close()


def apply_filter(filter_, ftype, row_dict):
    filtered = [re.search(reg, row_dict.get(key, ''))
               for key, reg in filter_.items()]
    print(ftype)
    if ftype == 'or':
        return any(filtered)
    elif ftype == 'and':
        return all(filtered)
    elif ftype == 'none':
        return not any(filtered)
    else:
        raise ValueError('Unknow filter type %s' % (ftype))


def main():
    args = parser.parse_args()
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(args.conf)
    filters = [
        ({k: re.compile(v) for k, v in config[section].items()
          if k != 'type'}, config[section].get('type', 'or'))
        for section in config.sections()
        if section.startswith('filter.')
    ]
    csv_opt = dict(config['csv'])
    out_file = args.out or 'out.csv'
    encoding = args.encoding or 'UTF-8'
    finder(args.csv_file, out_file, filters, encoding, csv_opt)
