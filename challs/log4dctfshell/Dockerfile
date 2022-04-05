FROM maven:3.5.0

RUN mkdir /app
ADD ./log4fdctfshell/ /app

WORKDIR /app

RUN mvn compile

EXPOSE 80
CMD ["mvn", "exec:java", "-Dexec.mainClass=very.secure.com.App"]
