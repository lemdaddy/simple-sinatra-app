FROM ruby:latest
RUN mkdir /hello-world
WORKDIR /hello-world
COPY Gemfile /hello-world/Gemfile
COPY config.ru /hello-world/config.ru
RUN bundle install
COPY . /hello-world

EXPOSE 3000

CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "3000"]