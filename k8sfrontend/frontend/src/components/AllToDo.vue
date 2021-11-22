<template>
  <div>
    <table align="center">
      <tr>
        <td>
        <template>
          <div id="app">
            <img :src="require('/tmp/kube/static/k8simage.jpg')" width="200" height="200"/>
          </div>
        </template>
        
          <!--img src="{% static 'k8simage.jpg' %}" alt="My image" /-->
        </td>
      </tr>

      <tr>
        <ApolloMutation
          :mutation="require('../graphql/insertTodo.gql')"
          :variables="{ newTodo }"
          @done="onDone"
        >
          <!-- v-slot -->
          <template v-slot="{ mutate }">
            <!--form v-on:submit.prevent="mutate()" -->
            <!--This caused form to be submitted twice-->
            <form>
              <td><input type="text" v-model="newTodo" id="id_textBox" /></td>
              <!--td><input type="button" value="CreateToDo" onclick="validate()" /></td-->
              <td><button @click="mutate()">CreateToDo</button></td>
            </form>
          </template>
        </ApolloMutation>
      </tr>
      <tr>
        <td>
          <!--ul id="id_list">
              <li v-for="todo in allList" :key="todo.text">
                {{ todo.text }}
              </li>
              <br />
            </ul-->
          <!--ApolloQuery
              :query="
                (gql) => gql`
                  query {
                    allList {
                      text
                    }
                  }
                `
              "
            -->
          <ApolloQuery :query="require('../graphql/allTodo.gql')">
            <!-- v-slot returns the result of the query with either loading, error, or with data-->
            <template v-slot="{ result: { loading, error, data } }">
              <div v-if="data">
                <ul id="id_list">
                  <li v-for="todo in allList" :key="todo.text">
                    {{ todo.text }}
                  </li>
                  <br />
                </ul>
              </div>
            </template>
          </ApolloQuery>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "AllToDo",
  data() {
    return {
      count: 7,
      newTodo: "",
    };
  },
  methods: {
    onDone() {
      this.$apollo.queries.allList.refetch();
      //alert("worked");
    },
  },
  apollo: {
    allList: gql`
      query {
        allList {
          text
        }
      }
    `,
  },
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

