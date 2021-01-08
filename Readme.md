#  CompLex

This site holds the data associated with the paper: CompLex — A New Corpus for Lexical Complexity Prediction from Likert Scale Data

available at: https://www.aclweb.org/anthology/2020.readi-1.9/

We are currently running a shared task on Lexical Complexity Prediction via SemEval using this data. As such, the data will be released according to the following release schedule:

 - Trial data available: July 31, 2020

 - Training data available: September 4, 2020

 - Test data available/Evaluation starts: January 11, 2021

See the task website for further information: https://sites.google.com/view/lcpsharedtask2021

See the CodaLab site to make a submission: https://competitions.codalab.org/competitions/27420

Currently, the trial, training and test data are available. The trial data comprises of 99 MWEs (29 bible, 33 biomed and 37 europarl) and 421 single word instances (143 bible, 135 biomed and 143 europarl). 

The training data comprises of 1,517 MWEs (505 bible, 514 biomed and 498 europarl) and 7,662 single word instances (2,574 bible, 2,576 biomed and 2,512 europarl). The training data is compressed and encrypted using 7zip (see: https://www.7-zip.org/), which is available on windows / linux. **You will need the password to decompress the 7zip archive, which can be obtained by registering for the shared task.**

The test data comprises of 184 MWEs (66 bible, 53 biomed and 65 europarl) and 917 single word instances (283 bible, 289 biomed and 345 europarl). It is compressedd and encrypted using 7zip as above. The password will be released to those registered for the task. The order of the test data has been randomised to prevent systems from overfitting to the data ordering. All submissions should be made via CodaLab as above. 

The trial and training data is arranged by token and sorted by complexity (i.e., instances with the same token appear together in groups, and the groups are sorted by the complexity of the lowest scored item). Tokens that appear in one partition will not appear in another partition. We have deliberately included more than one instance of a token where possible to identify places where the context affects the complexity of a word.  Consider, for example, the following two sentences from the trial data:

 - We now have a proposal on the *table* which lays down strict emissions values for the next ten years and which simultaneously creates clarity and incentives for technological innovations.	
 - Mr President, in coordination with other groups, I would like to *table* an oral amendment concerning the draft bill in the Duma to ignore certain rulings of the European Court of Human Rights.	

When *table* is used as a noun  in the first sentence (albeit in an abstract sense) it receives a score of 0.01 indicating it is very easily understood. However, when it is used as a verb in the second, it is scored at 0.23, indicating a more difficult word to comprehend.

The data comes from three sources: biblical text, biomedical articles and proceedings of the European Parliament. These sources were selected as they contain a natural mixture of common language and difficult to understand expressions, whilst each containing vastly different domain-specific vocabulary. Systems must submit on all three sub-corpora

In addition to the single word task, we have also annotated multi-word expressions. These form a second track for our shared task. Systems which submit to both the single and multi word tracks will be additionally evaluated on the joint scores on both corpora. 

# Baselines

To aid those participating in the shared task with a reasonable estimation of performance we have released the following baselines combining log word frequency from SUBTLEX and word length. Features were averaged for each token in a MWE. The training set was used for training and the trial set was used for evaluation. Each feature, or combination of features was passed through linear regression. The complexity-averge gives the same 'average complexity' value, learned from the training set to each value in the trial set. We report on the following metrics:

 - Pearson's R (R)
 - Spearman's Rho (Rho)
 - Mean Absolute Error (MAE)
 - Mean Squared Error (MSE)
 - R-squared (R2)
 
 ### Task 1 - Single Words

| Features                   |R|Rho|MAE|MSE|R2|
| -------------              |:---:| :---:| :---:| :---:| :---:|
| Complexity-average         |  - |	 - |	 0.1049 |	 0.0189 |	 0.0007 |
| Length                     |  0.1589 |	 0.2196 |	 0.1035 |	 0.0185 |	 0.0207 |
| Log Frequency              |  0.5287 |	 **0.5263** |	 0.0870 |	 0.0136 |	 0.2779 |
| Log Frequency and Length   |  **0.5376** |	 0.5251 |	 **0.0867** |	 **0.0135** |	 **0.2864** |

### Task 2 - MWEs

| Features                   |R|Rho|MAE|MSE|R2|
| -------------              |:---:| :---:| :---:| :---:| :---:|
| Complexity-average         | -       |	 -     |	 0.1228 |  0.0234	|  0.0000 |
| Length                     | 0.4822 	| 0.4642 |	 0.1104 |	 0.0185 |	 0.2083 |
| Log Frequency              | 0.6571 	| 0.6345 |	 0.0924 |	 0.0140 |	 0.4030 |
| Log Frequency and Length   | **0.6969** 	| **0.6713** |	 **0.0908** |	 **0.0129** |	 **0.4485** |

