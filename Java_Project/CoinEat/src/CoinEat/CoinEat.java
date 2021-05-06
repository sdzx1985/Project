package CoinEat;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class CoinEat extends JFrame {
	private Image bufferImage;
	private Graphics screenGraphic;

	private Clip clip;

	private Image backgroundImage = new ImageIcon("src/images/mainScreen.png").getImage();
	private Image player = new ImageIcon("src/images/player.png").getImage();
	private Image coin = new ImageIcon("src/images/coin.png").getImage();

	private int playerX, playerY;
	private int playerWidth = player.getWidth(null);
	private int playerHeight = player.getHeight(null);

	private int coinX, coinY;
	private int coinWidth = coin.getWidth(null);
	private int coinHeight = coin.getHeight(null);

	private int score;

	private boolean up, down, left, right;

	public CoinEat() {
		setTitle("Coin Eat");
		// setVisible(true);
		setSize(500, 500);
		setLocationRelativeTo(null);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e) {
				switch (e.getKeyCode()) {
					case KeyEvent.VK_W:
						up = true;
						break;
					case KeyEvent.VK_S:
						down = true;
						break;
					case KeyEvent.VK_A:
						left = true;
						break;
					case KeyEvent.VK_D:
						right = true;
						break;
				}
			}

			public void keyReleased(KeyEvent e) {
				switch (e.getKeyCode()) {
					case KeyEvent.VK_W:
						up = false;
						break;
					case KeyEvent.VK_S:
						down = false;
						break;
					case KeyEvent.VK_A:
						left = false;
						break;
					case KeyEvent.VK_D:
						right = false;
						break;
				}
			}
		});
		Init();
		setVisible(true);
		while (true) {
			try {
				Thread.sleep(20);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			keyProcess();
			crashCheck();
		}
	}

	public void Init() {
		score = 0;
		playerX = (500 - playerWidth) / 2;
		playerY = (500 - playerHeight) / 2;

		coinX = (int) (Math.random() * (501 - playerWidth));
		coinY = (int) (Math.random() * (501 - playerHeight - 30)) + 30;

		playSound("src/audio/backgroundMusic.wav", true);
	}

	public void keyProcess() {
		if (up && playerY - 3 > 30)
			playerY -= 3;
		if (down && playerY + playerHeight + 3 < 500)
			playerY += 3;
		if (left && playerX - 3 > 30)
			playerX -= 3;
		if (right && playerX + playerWidth + 3 < 500)
			playerX += 3;
	}

	public void crashCheck() {
		if (playerX + playerWidth > coinX && coinX + coinWidth > playerX && playerY + playerHeight > coinY
				&& coinY + coinHeight > playerY) {
			score += 100;
			playSound("src/audio/CoinEat_src_audio_getCoin.wav", false);
			coinX = (int) (Math.random() * (501 - playerWidth));
			coinY = (int) (Math.random() * (501 - playerHeight - 30)) + 30;
			if (score == 2000)
				System.exit(0);
		}
	}

	public void playSound(String pathName, boolean isLoop) {
		try {
			clip = AudioSystem.getClip();
			File audioFile = new File(pathName);
			AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
			clip.open(audioStream);
			clip.start();
			if (isLoop)
				clip.loop(clip.LOOP_CONTINUOUSLY);
		} catch (LineUnavailableException e) {
			e.printStackTrace();
		} catch (UnsupportedAudioFileException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void paint(Graphics g) {
		bufferImage = createImage(500, 500);
		screenGraphic = bufferImage.getGraphics();
		screenDraw(screenGraphic);
		g.drawImage(bufferImage, 0, 0, null);

	}

	public void screenDraw(Graphics g) {
		g.drawImage(backgroundImage, 0, 0, null);
		g.drawImage(coin, coinX, coinY, null);
		g.drawImage(player, playerX, playerY, null);
		g.setColor(Color.WHITE);
		g.setFont(new Font("Arial", Font.BOLD, 40));
		g.drawString("SCORE : " + score, 30, 80);
		this.repaint();
	}

	public static void main(String[] args) {
		new CoinEat();
	}

}
