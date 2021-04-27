package CoinEat;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class CoinEat extends JFrame{
	
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
	
	public CoinEat() {
		setTitle("Coin Eat");
//		setVisible(true);
		setSize(500, 500);
		setLocationRelativeTo(null);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Init();
		setVisible(true);
	}
	
	public void Init() {
		score = 0;
		playerX = (500 - playerWidth)/2;
		playerY = (500 - playerHeight)/2;
		
		coinX = (int)(Math.random()*(501-playerWidth));
		coinY = (int)(Math.random()*(501-playerHeight-30))+30;
	}
	public void paint(Graphics g) {
		g.drawImage(backgroundImage, 0, 0, null);
		g.drawImage(coin, coinX, coinY, null);
		g.drawImage(player, playerX, playerY, null);
		g.setColor(Color.WHITE);
		g.setFont(new Font("Arial", Font.BOLD, 40));
		g.drawString("SCORE : "+score, 30, 80);
	}
	
	public static void main(String[] args) {
		new CoinEat();

	}

}
