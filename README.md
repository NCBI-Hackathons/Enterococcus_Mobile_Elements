# AMR_Mobile_Element_Education
Development of a FAIR Educational Resource for Tracking AMR Genes in Mobile Elements using Enterococcae as an Example  

Background
•	Mobile elements such as transposons and plasmids are important features of bacterial genomes. 
  o	They often contain resistance genes, which can compromise antimicrobial therapy
  o	We seek to use Enterococcus as a test case to identify these transposons and plasmids. 
•	The goal is to create a tool to be integrated into NCBI’s Pathogen Detection pipeline

Methods
•	15,000 SRA submissions of Enterococcus faecalis and Enterococcus faecium were included
  o	SKESA was used for assembly
  o	AMRFinder was used to identify resistance genes
  o	BLAST analysis
    	For presence of known plasmid and transposon signatures, using x cutoffs
  o	gff search
    	Looking for annotations associated with mobile elements (terms such as repA, repB, repC, conjugative, and traA, traB, and traC)
  o	Comparison to known plasmids
    	BLAST was done to known plasmid sequences, to ensure validity of results

Conclusion
•	Combined with SKESA assemblies and AMRFinder outputs, the addition of mobile element analysis to the Pathogen Detection pipeline will be extremely useful in identifying potential transmissibility of resistance genes
  o	Enterococcus provides a valuable test case for future roll out of this tool across all pathogens
