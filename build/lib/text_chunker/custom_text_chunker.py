from time import perf_counter
from langchain.text_splitter import RecursiveCharacterTextSplitter


class FixedLengthChunker():
    
    def chunk_text(self,chunk_size_arg,chunk_overlap_arg,text)-> list[str]:
        start_time = perf_counter()
        lenz= len(text)
        print(f"\t\t\tStarted the chunking the text of len {lenz} ")
        # Initialize the text splitter with custom parameters
        custom_text_splitter_n = RecursiveCharacterTextSplitter(
            # Set custom chunk size
            chunk_size = chunk_size_arg,
            chunk_overlap  = chunk_overlap_arg,
            # Use length of the text as the size measure
            length_function = len,
            # Use only "\n\n" as the separator
            separators = ['\n']

        )       
        # Create the chunk    
        final_texts= custom_text_splitter_n.split_text(text)
        end_time = perf_counter()
        print(len(final_texts))
        print(f"\t\t\tEnded the chunking the text , Total time taken for text splitter {end_time - start_time}")
        return final_texts