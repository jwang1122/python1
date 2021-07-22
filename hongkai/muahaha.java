public class muahaha {

    public static void main(String[] args) {
        System.out.println("where's the run button");
    }
}

//dont mind me 
// package com.huaxia.blackjack;

// import java.util.ArrayList;
// import java.util.List;
// import java.util.Scanner;

// public class Player {
// 	protected String name;
// 	protected List<Card> hand = new ArrayList<>();
	
// 	public Player(String name) {
// 		this.name = name;
// 	}
	
// 	public boolean hit() {
// 		boolean needMoreCard = false;
// 		System.out.print(name + ", do you want to hit? (y/n) ");
// 		Scanner input = new Scanner(System.in);
// 		String answer = input.nextLine();
// 		input.close();
// 		needMoreCard = answer.equals("y");
// 		return needMoreCard;
// 	}
	
// 	public void addCardToHand(Card card) {
// 		hand.add(card);
// 	}
	
// 	public void cleanHand() {
// 		hand.clear();
// 	}
	
// 	public int getHandValue() {
// 		int value = 0;
// 		for(Card card:hand) {
// 			value += card.getValue();
// 		}
// 		if(value>21) { // busted!
// 			if (isAceInHand()) {
// 				value -= 10; // correct my Ace from 11 to 1
// 			}
// 		}
// 		return value;
// 	}
	
// 	//Homework: write unit test to test this method
// 	private boolean isAceInHand() {
// 		boolean flag = false; // assume there is no Ace in my hand
// 		for (Card card : hand) {
// 			if(card.face.equals("A")) {
// 				flag = true;
// 				break;
// 			}
// 		}
// 		return flag;
// 	}
	
// 	public String showHand() {
// 		String myHand = name + "{";
// 		for(Card card: hand) { // for-each loop
// 			myHand += card + " ";
// 		}
// 		myHand += "}";
// 		return myHand;
// 	}
	
// 	@Override
// 	public String toString() {
// 		return name;
// 	}

// 	public Integer getHandSize() {
// 		return hand.size();
// 	}

// 	public String getName() {
// 		return name;
// 	}
	
// 	public static void main(String[] args) {
// 		Player john = new Player("Johnsy");
// 		System.out.println(john.hit());
// 	}
// }
