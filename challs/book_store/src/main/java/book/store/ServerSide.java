package book.store;

import java.io.IOException;
import java.io.OutputStream;
import java.net.*;
import java.security.MessageDigest;

import java.math.BigInteger;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.util.*;
import java.io.*;

public class ServerSide {
	StringBuilder index_page_html;
	StringBuilder landing_page_html;
	StringBuilder book_json;
	HttpServer server;
	int server_port;
	Logger logger;

	public ServerSide(int server_port) {
		// setup server	
		try {

			this.landing_page_html = new StringBuilder();
			this.index_page_html = new StringBuilder();
			this.book_json = new StringBuilder();
			this.logger = new Logger(this.getClass().getName());
			this.server_port = server_port;

			this.loadIndexPage();
			this.loadLandingPage();
			this.loadBook();
			this.setupRoutes();

		} catch (Exception e) {
			logger.error("FATAL :(");
			logger.error(e.getMessage());
		}
	}

	private void loadIndexPage() {	
		InputStream is = ServerSide.class.getResourceAsStream("/auth.html");
		Scanner s = new Scanner(is).useDelimiter("\\A");

		while(s.hasNext())
			this.index_page_html.append(s.next());

		logger.debug("Auth page loaded in memory");

		s.close();
	}

	private void loadLandingPage() {
		InputStream is = ServerSide.class.getResourceAsStream("/home.html");
		Scanner s = new Scanner(is).useDelimiter("\\A");

		while(s.hasNext())
			landing_page_html.append(s.next());

		logger.debug("Landing page loaded in memory");

		s.close();
	}

	private void loadBook() {
		InputStream is = ServerSide.class.getResourceAsStream("/book.json");
		Scanner s = new Scanner(is).useDelimiter("\\A");

		while(s.hasNext())
			book_json.append(s.next());

		logger.debug("Book contents loaded in memory");

		s.close();
	}

	private void setupRoutes() throws Exception {
		this.server = HttpServer.create(new InetSocketAddress(this.server_port), 0);

		// Static pages
		this.server.createContext("/", new LoginPageServer());
		this.server.createContext("/home.html", new LandingPageServer());

		// Api
		this.server.createContext("/login", new LoginHandler());
		this.server.createContext("/book", new BookHandler());

		this.server.setExecutor(null); // creates a default executor
		this.server.start();

		logger.info("Started web server!");
	}


	public HashMap<String, String> splitQuery(String requestUri) throws UnsupportedEncodingException {
		HashMap<String, String> query_pairs = new HashMap<String, String>();
		String[] pairs = requestUri.split("&");

		for (String pair : pairs) {
			int idx = pair.indexOf("=");
			query_pairs.put(URLDecoder.decode(pair.substring(0, idx), "UTF-8"), URLDecoder.decode(pair.substring(idx + 1), "UTF-8"));
		}

		return query_pairs;
	}
	public static String getMd5(String input)
	{
		try {

			// Static getInstance method is called with hashing MD5
			MessageDigest md = MessageDigest.getInstance("MD5");

			// digest() method is called to calculate message digest
			//  of an input digest() return array of byte
			byte[] messageDigest = md.digest(input.getBytes());

			// Convert byte array into signum representation
			BigInteger no = new BigInteger(1, messageDigest);

			// Convert message digest into hex value
			String hashtext = no.toString(16);
			while (hashtext.length() < 32) {
				hashtext = "0" + hashtext;
			}
			return hashtext;
		} 

		// For specifying wrong message digest algorithms
		catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	public boolean parseRequest(String requestUri) throws UnsupportedEncodingException {
		HashMap<String, String> query_params = splitQuery(requestUri);
		String username = (String) query_params.get("username");
		String password = (String) query_params.get("password");
		String hashed_username =  getMd5(username);
		String hashed_password = getMd5(password);
		String mssg = "username: " + username + ", password: " + password;

		logger.info(mssg);
		/*
		 * They didn't pay me this month so screw them, leaving company, somebody else fix auth..
		 */
		if( hashed_username.equalsIgnoreCase("21232f297a57a5a743894a0e4a801fc3") && hashed_password.equalsIgnoreCase("21232f297a57a5a743894a0e4a801fc3") )
			return true;

		return false;
	}

	static class LoginHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException, UnsupportedEncodingException  {	

			// parse request
			String response;
			if(book.store.App.ss.parseRequest(t.getRequestURI().getQuery())) {
				response = "cool :)";
				t.getResponseHeaders().add("auth", System.getenv("WEB_COOKIE"));
				book.store.App.ss.logger.info("Authorized access!");
				t.sendResponseHeaders(200, response.length());

				// redirect
			} else {
				response = "sad day today for you :(";
				book.store.App.ss.logger.warning("Unauthorized access!");
				t.sendResponseHeaders(401, response.length());
			}

			// send response
			OutputStream os = t.getResponseBody();
			os.write(response.getBytes());
			os.close();
		}
	}

	static class BookHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException {	
			StringBuilder response = book.store.App.ss.book_json;

			t.getResponseHeaders().add("Content-Type", "application/json");
			t.sendResponseHeaders(200, response.toString().getBytes().length);
			OutputStream os = t.getResponseBody();
			os.write(response.toString().getBytes());
			os.close();
		}
	}

	static class LoginPageServer implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException {	
			StringBuilder response = book.store.App.ss.index_page_html;

			t.getResponseHeaders().add("Content-Type", "text/html");
			t.sendResponseHeaders(200, response.toString().getBytes().length);
			OutputStream os = t.getResponseBody();
			os.write(response.toString().getBytes());
			os.close();
		}
	}

	static class LandingPageServer implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException {	
			StringBuilder response = book.store.App.ss.landing_page_html;

			t.getResponseHeaders().add("Content-Type", "text/html");
			t.sendResponseHeaders(200, response.length());
			OutputStream os = t.getResponseBody();
			os.write(response.toString().getBytes());
			os.close();
		}
	}
}
