#  CompLex

This site holds the data associated with the paper: CompLex — A New Corpus for Lexical Complexity Prediction from Likert Scale Data

available at: https://www.aclweb.org/anthology/2020.readi-1.9/

This data is released under CC-BY: https://creativecommons.org/licenses/by/4.0/

We ran a shared task on Lexical Complexity Prediction via SemEval using this data. The data was released according to the following schedule:

 - Trial data available: July 31, 2020

 - Training data available: September 4, 2020

 - Test data available/Evaluation starts: January 11, 2021

See the task website for further information: https://sites.google.com/view/lcpsharedtask2021

See the CodaLab site to view submissions: https://competitions.codalab.org/competitions/27420

The script evaluate.py is the same evaluation script that was used as part of the shared task. You can run this by calling "python evaluate.py <results_path>/res/ <reference_path>/ref/" where res and ref are directories containing the system's results and the reference labels respectively.

The trial, training and test data are available. The trial data comprises of 99 MWEs (29 bible, 33 biomed and 37 europarl) and 421 single word instances (143 bible, 135 biomed and 143 europarl). 

The training data comprises of 1,517 MWEs (505 bible, 514 biomed and 498 europarl) and 7,662 single word instances (2,574 bible, 2,576 biomed and 2,512 europarl).

The test data comprises of 184 MWEs (66 bible, 53 biomed and 65 europarl) and 917 single word instances (283 bible, 289 biomed and 345 europarl). It is compressedd and encrypted using 7zip as above. The password will be released to those registered for the task. The order of the test data has been randomised to prevent systems from overfitting to the data ordering. All submissions should be made via CodaLab as above. 

The trial and training data is arranged by token and sorted by complexity (i.e., instances with the same token appear together in groups, and the groups are sorted by the complexity of the lowest scored item). Tokens that appear in one partition will not appear in another partition. We have deliberately included more than one instance of a token where possible to identify places where the context affects the complexity of a word.  Consider, for example, the following two sentences from the trial data:

 - We now have a proposal on the *table* which lays down strict emissions values for the next ten years and which simultaneously creates clarity and incentives for technological innovations.	
 - Mr President, in coordination with other groups, I would like to *table* an oral amendment concerning the draft bill in the Duma to ignore certain rulings of the European Court of Human Rights.	

When *table* is used as a noun  in the first sentence (albeit in an abstract sense) it receives a score of 0.01 indicating it is very easily understood. However, when it is used as a verb in the second, it is scored at 0.23, indicating a more difficult word to comprehend.

The data comes from three sources: biblical text, biomedical articles and proceedings of the European Parliament. These sources were selected as they contain a natural mixture of common language and difficult to understand expressions, whilst each containing vastly different domain-specific vocabulary. S

