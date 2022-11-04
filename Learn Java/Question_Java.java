public class Question
{
	int correctAnswer;
	int playerAnswer;
	int imageId;
	String questionText;
	String answer0;
	String answer1;
	String answer2;
	String answer3;

	Question(int imageIdentifier, String questionString, String answerZero, 
		String answerOne, String asnwerTwo, String answerThree, int correctAnswerIndex)
	{
		imageId = imageIdentifier;
		questionText = questionString;
		answer0 = answerZero;
		answer1 = answerOne;
		answer2 = answerTwo;
		answer3 = answerThree;
		correctAnswer = correctAnswerIndex;
		playerAnswer = -1;
	}
}