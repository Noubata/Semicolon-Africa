public class CollectInput{
	public static void main(String[]args){
	
	int [] numbers1 = {10, 9, 13, 2, 14};
	int [] numbers2 = {36, 14, 57, 23, 43, 0, -1};

	int largest = numbers1[0];
	for(int toGet = 0; toGet<=4; toGet++){
	if(numbers1[toGet]>largest){
	largest=numbers1[toGet];
	}
	}
	System.out.println(largest);

	int largest1 = numbers2[0];
	for(int toGet1 = 0; toGet1<=4; toGet1++){
	if(numbers2[toGet1]>largest1){
	largest1=numbers2[toGet1];
	}
	}
	System.out.print(largest1);








}
}