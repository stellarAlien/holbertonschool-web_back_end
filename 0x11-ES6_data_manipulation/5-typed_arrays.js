export default function createInt8TypedArray(length, position,  value){
	if (typeof length !== 'number') {
		throw new Error('length must be a nubmer');
	}
	if (typeof position !== 'number') {
		throw new Error('position msut be a number')
	}
	if (typeof value !== 'number') {
		throw new Error('value msut be a number')
	}
	try {
		const buffer = new ArrayBuffer(length);
		const view =  new DataView(buffer).setInt8(position, value);
		return view;
	} catch(err){
		throw new Error('Position outisde range');
	}
  }