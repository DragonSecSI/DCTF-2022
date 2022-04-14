package book.store;

public class App {

	static ServerSide ss; 
	public static void main( String[] args ) throws Exception {
		// display welcome art
		Art art = new Art();
		System.out.println();
		art.printTextArt("HiddenBook :)", Art.ART_SIZE_SMALL);

		// Start web server
		// two threads one for file checking and one for server process
		ss = new ServerSide(Integer.parseInt(System.getenv("SERVER_PORT")));

		// start log job
		LogJob lj = new LogJob(book.store.App.ss.getClass().getName());
		lj.start();
	}
}
