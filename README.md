# logs_analysis

an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1.Download and install Vagrant 2.2.0
2.Download Vagrantfile and install the virtual box:

'''
$ git clone https://github.com/udacity/fullstack-nanodegree-vm.git FSND_VM
$ cd FSND_VM/vagrant
$ vagrant up
$ vagrant ssh

'''
3. download the data base  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
4.unzip this file after downloading it.


### Installing

1. make shure you are start the virtual by vagrant up and log in by ssh then ''' cd /vagrant '''
2. clone this repo 
'''
git clone https://github.com/hadeelkh/logs_analysis.git
'''
3. load the data by
'''
psql -d news -f newsdata.sql

'''

4. Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.
'''
\dt — display tables — lists the tables that are available in the database.
\d table — (replace table with the name of a table) — shows the database schema for that particular table.

'''
5.Install the project requirements:
'''
$ pip3 install -r requirements.txt
'''

## Running the tests

to run the program you should be in the newsdata diroctory then

'''
python3 main.py

'''
## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/hadeelkh/logs_analysis/tags). 

## Authors

* **hadeel khaled** - *Initial work* - [hadeelkh](https://github.com/hadeelkh)

See also the list of [contributors](https://github.com/hadeelkh/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
