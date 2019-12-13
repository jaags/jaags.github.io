
dependency :
     ruby
     bundle 

deployment dependency:
    bundle 
    rake

update ruby:

    bundle install => to install all the packages provided in the gemfile

    sudo apt-get install build-essential patch ruby-dev zlib1g-dev liblzma-dev


Running :
     $ bundle exec jekyll serve --trace