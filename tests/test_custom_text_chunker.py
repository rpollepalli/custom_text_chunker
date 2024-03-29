from text_chunker.custom_text_chunker import FixedLengthChunker

def test_chunk_text():
    text = """One of the most important things I didn't understand about the world 
    when I was a child is the degree  
    to which the returns for performance are superlinear."""
    assert len(FixedLengthChunker().chunk_text(100,5,text)) ==2