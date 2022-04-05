#-- firstly compile project
mvn compile
#-- secondly run project
mvn exec:java -Dexec.mainClass=very.secure.com.App
