const AWS = require("aws-sdk")
AWS.config.update({region: "eu-central-1"})

const dynamodb = new AWS.DynamoDB()

// dynamodb.listTables({}, (err, data) => {
//     if (err){
//         console.log(err)
//     } else {
//         console.log(data)
//     }

// })

dynamodb.describeTable({ TableName: "td_notes" }, (err, data) => {
     if (err){
         console.log(err)
     } else {
         console.log(JSON.stringify(data, null, 2))
     }   
})