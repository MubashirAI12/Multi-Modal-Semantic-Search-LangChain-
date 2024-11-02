from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import  RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from pydantic import BaseModel



def semantic_search_rag(query, vectorstore, llm_chain_model):
    try:
        num_chunks= 2
        retriever= vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": num_chunks})

        # retriever = MultiQueryRetriever.from_llm(llm=llm_chain_model, 
        #                                  retriever=vectorstore.as_retriever(search_kwargs={"k": num_chunks}))
        # compressor = LLMChainExtractor.from_llm(llm_chain_model)
        # retriever = ContextualCompressionRetriever(
        #     base_compressor=compressor, base_retriever=retriever
        # )
        template = """Answer the question and in your own words as truthfully as possible from the following pieces of context:
        context: {context}

        question: {question}

        """
        prompt = ChatPromptTemplate.from_template(template)
        setup_and_retrieval = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        )
        output_parser= StrOutputParser()
        # chain = setup_and_retrieval | prompt | model | output_parser
        context=  setup_and_retrieval.invoke(query)
        prompt_answer= prompt.invoke({'context':context, 'question': query})
        model_answer= llm_chain_model.invoke(prompt_answer)
        response= output_parser.invoke(model_answer)
        return response

    except Exception as e:
        raise Exception(f'Error: {e}')   
