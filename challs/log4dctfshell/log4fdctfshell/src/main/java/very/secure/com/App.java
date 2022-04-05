package very.secure.com;

import java.io.IOException;
import java.io.OutputStream;
import java.net.*;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.Map;
import java.util.Collections;
import java.util.stream.Collectors;

import java.util.*;
import java.io.*;
// TODO
// https://www.codeproject.com/Tips/1040097/Create-a-Simple-Web-Server-in-Java-HTTP-Server

public class App {
	
	static String index_page_html;
    static Logger logger = LogManager.getLogger(very.secure.com.App.class);
	public static void main( String[] args ) throws Exception {

		// set properties

		// Read index file
		InputStream is = App.class.getResourceAsStream("/index.html");
		Scanner s = new Scanner(is).useDelimiter("\\A");
		index_page_html = s.hasNext() ? s.next() : "";

		HttpServer server = HttpServer.create(new InetSocketAddress(80), 0);
		server.createContext("/index.html", new MyHandler());
		server.createContext("/login", new LoginHandler());
		server.setExecutor(null); // creates a default executor
		server.start();
	}

	static class LoginHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException, UnsupportedEncodingException  {	

			// parse request
			parseRequest(t.getRequestURI().getQuery());
			// send response
			String response = "try harder:)";
			t.sendResponseHeaders(200, response.length());
			OutputStream os = t.getResponseBody();
			os.write(response.getBytes());
			os.close();
		}

		public boolean parseRequest(String requestUri) throws UnsupportedEncodingException {
			HashMap query_params = splitQuery(requestUri);

			String username = (String) query_params.get("username");
			String password = (String) query_params.get("password");

			String mssg = "username: " + username + ", password: " + password;
		
			System.out.println(mssg);


			logger.error(mssg);

			return true;
		}

		public static HashMap<String, String> splitQuery(String requestUri) throws UnsupportedEncodingException {
			HashMap<String, String> query_pairs = new HashMap<String, String>();
			String[] pairs = requestUri.split("&");
			for (String pair : pairs) {
				int idx = pair.indexOf("=");
				query_pairs.put(URLDecoder.decode(pair.substring(0, idx), "UTF-8"), URLDecoder.decode(pair.substring(idx + 1), "UTF-8"));
			}
			return query_pairs;
		}
	}


	static class MyHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException {	
			logger.error("New connection to server!");
			String response = index_page_html;

			t.sendResponseHeaders(200, response.length());
			OutputStream os = t.getResponseBody();
			os.write(response.getBytes());
			os.close();
		}
	}


	public void destroy() {
	}
}

