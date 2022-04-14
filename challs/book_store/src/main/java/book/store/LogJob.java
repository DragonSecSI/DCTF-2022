package book.store;

import java.io.File;

public class LogJob extends Thread {
	String filename;

	public LogJob(String filename) {
		this.filename = filename;
	}

	private void deleteLogFile() {
		File f = new File(this.filename + ".log");

		if(f.delete())
			book.store.App.ss.logger.info("Successfully deleted logfile!");
		else 
			book.store.App.ss.logger.warning("File must be empty!");
	}

	public void run() {
		while(true) {
			try {
				Thread.sleep(1000 * 120);
			} catch (Exception e) {
				System.err.println(e.getMessage());
			}
			deleteLogFile();
		}
	}

}
