import axios from "axios";
import baseUrl from "../config";

const state = {
    customer: {},
    customers: {
        data: [],
        pagination: {
          num_pages: 1,
          current_page: 1
        }
    }
};

const getters = {
    getCustomer: state => state.customer,
    getCustomers: state => state.customers
};

const actions = {
    async get_customer({ commit }, id) {
        const res = await axios.get(`${baseUrl}customer/${id}/`);
        commit("SET_CUSTOMER", res.data);
    },
    async get_customers({ commit }, page) {
        let url = `${baseUrl}customer/`;
        if(page !== undefined)
        url += `?page=${page}`
        const res = await axios.get(url);
        commit("SET_CUSTOMERS", res.data);
    },
    async get_customers_without_pages({ commit }) {
        const res = await axios.get(`${baseUrl}customer/get-without-pages/`);
        commit("SET_CUSTOMERS", res.data);
    },
    async add_customer({ commit }, customer) {
        const res = await axios.post(`${baseUrl}customer/`, customer);
        commit("SET_CUSTOMER", res.data);
    },
    async update_customer({ commit }, customer) {
        const res = await axios.put(`${baseUrl}customer/${customer.id}/`, customer);
        commit("SET_CUSTOMER", res.data);
    },
    async delete_customer({ commit }, id) {
        const res = await axios.delete(`${baseUrl}customer/${id}/`);
    }
};

const mutations = {
    SET_CUSTOMERS: (state, customers) => state.customers = customers,
    SET_CUSTOMER: (state, customer) => state.customer = customer,

};

export default {
    state,
    getters,
    actions,
    mutations
};
