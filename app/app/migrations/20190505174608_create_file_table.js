
exports.up = function(knex, Promise) {

    return knex.schema.createTable('file', function(t) {
        t.increments('id').primary()
        t.string('username').notNullable()
        t.string('passowrd').notNullable()
        t.timestamps(false,true)
    })
  
};

exports.down = function(knex, Promise) {
  
        return knex.schema.dropTableIfExists('file')
};
