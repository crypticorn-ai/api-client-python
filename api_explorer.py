import pprint
import streamlit as st
from api_client import ApiClient
import pandas as pd
import inspect

api_client = ApiClient()


def get_class_vars(class_instance, exclude_methods: list) -> dict:
    methods = inspect.getmembers(class_instance, predicate=inspect.ismethod)
    methods = [m for m in methods if
               not (m[0].startswith('__') and m[0].endswith('__')) and m[0] not in exclude_methods]

    res = {}
    for m in methods:
        function_name = m[0],
        function_ref = m[1]
        res.update({
            function_name[0]: {
                "func_ref": function_ref,
                "args": function_ref.__annotations__
            }
        })

    return res


class_vars = get_class_vars(api_client, exclude_methods=["get_response"])


def main():
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    st.header("Api Explorer :books:")
    load_explorer_dropdown()


def load_sidebar():
    with st.sidebar:
        st.file_uploader("Upload you CSV file", type="csv", accept_multiple_files=True)
        st.subheader("Your documents")
        if st.button("Process"):
            with st.spinner("Processing"):
                print("some actions")


def load_explorer_dropdown():
    selection = st.selectbox("Select endpoint", options=list(class_vars.keys()))
    create_submit_form(selection)

    if selection == "UBC":
        form = st.form("filing form")

        with form:
            ticker = st.text_input("Ticker", placeholder="BTCUSDT")
            entries = st.number_input("Entries", placeholder="Number of entries", min_value=1)
            submit_button = st.form_submit_button("submit", type="primary")

        if submit_button:
            with st.spinner("Processing"):
                tab1, tab2, tab3 = st.tabs(["Dataframe", "Line Chart", "Bar Chart"])
                df = api_client.get_bc_historical(ticker, entries, reverse=False)
                df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

                with tab1:
                    st.dataframe(df)
                with tab2:
                    st.line_chart(df, x="timestamp", y="open_15m")
                with tab3:
                    st.bar_chart(df, x="timestamp", y="open_15m")


def create_submit_form(selection: str):
    mapping = {
        int: st.number_input,
        str: st.text_input,
        bool: st.checkbox,
        list: st.text_input,
    }

    form = st.form("test form")
    with form:
        collected_data = []

        args = class_vars[selection]["args"]
        for arg in args:
            if arg == "return":
                continue

            if args[arg] is int:
                res = mapping[args[arg]](arg, min_value=1)
            else:
                res = mapping[args[arg]](arg)

            collected_data.append(res)

        button_clicked = form.form_submit_button("submit", type="primary")

        if button_clicked:
            df = class_vars[selection]["func_ref"](*collected_data)
            if not isinstance(df, pd.DataFrame):
                st.markdown(str(df))
            else:
                st.dataframe(df)


if __name__ == '__main__':
    main()
