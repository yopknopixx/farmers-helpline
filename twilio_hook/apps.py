from django.apps import AppConfig
from haystack.pipelines import Pipeline, GenerativeQAPipeline
from haystack.nodes import (
    Crawler,
    PreProcessor,
    ElasticsearchRetriever,
    FARMReader,
    DensePassageRetriever,
    RAGenerator,
    Seq2SeqGenerator,
)
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.utils import print_answers


class TwilioHookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "twilio_hook"


class QueryAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "query_app"
    document_store = ElasticsearchDocumentStore(
        host="localhost",
        username="",
        password="",
        index="document",
        return_embedding=True,
    )
    # reader =  FARMReader(model_name_or_path="deepset/bert-large-uncased-whole-word-masking-squad2")
    retriever = DensePassageRetriever(
        document_store=document_store,
        query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
        passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
        max_seq_len_query=64,
        max_seq_len_passage=256,
        batch_size=16,
        use_gpu=True,
        embed_title=True,
        use_fast_tokenizers=True,
    )
    generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")
    query_pipeline = GenerativeQAPipeline(generator=generator, retriever=retriever)


"""def home_view(request):
    print(request.GET)"""
