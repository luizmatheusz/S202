{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'titulo',
      'autor',
      'ano',
      'preco'
    ],
    properties: {
      titulo: {
        bsonType: 'string',
        description: 'deve ser uma string'
      },
      autor: {
        bsonType: 'string',
        description: 'deve ser uma string'
      },
      ano: {
        bsonType: 'int',
        description: 'deve ser um inteiro'
      },
      preco: {
        bsonType: 'double',
        description: 'deve ser um ponto flutuante'
      }
    }
  }
}