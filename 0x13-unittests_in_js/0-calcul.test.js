const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  describe('two Integers', () => {
    it('should return 4', () => {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('one round', () => {
    it('should return 5', () => {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe('one round 2', () => {
    it('should return 5', () => {
      assert.strictEqual(calculateNumber(3.7, 1), 5);
    });
  });

  describe('one round floor', () => {
    it('should return 4', () => {
      assert.strictEqual(calculateNumber(1, 3.3), 4);
    });
  });

  describe('one round floor 2', () => {
    it('should return 4', () => {
      assert.strictEqual(calculateNumber(3.3, 1), 4);
    });
  });

  describe('two round', () => {
    it('should return 5', () => {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe('two round again', () => {
    it('should return 6', () => {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe('two round reversed', () => {
    it('should return 5', () => {
      assert.strictEqual(calculateNumber(3.7, 1.2), 5);
    });
  });

  describe('two round again floor both', () => {
    it('should return 3', () => {
      assert.strictEqual(calculateNumber(1.2, 2.1), 3);
    });
  });
});
