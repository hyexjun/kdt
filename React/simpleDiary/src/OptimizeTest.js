import { useState, useEffect } from 'react';

const Textview = ({ text }) => {
  return <div>{text}</div>;
};

const Countview = ({ count }) => {
  return <div>{count}</div>;
};

const OptimizeTest = () => {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  return (
    <div style={{ padding: 50 }}>
      <div>
        <h2>count</h2>
        <Countview count={count} />
        <button
          onClick={() => {
            setCount(count + 1);
          }}
        >
          +
        </button>
      </div>
      <div>
        <h2>text</h2>
        <Textview text={text} />
        <input
          value={text}
          onChange={(event) => {
            setText(event.target.value);
          }}
        />
      </div>
    </div>
  );
};

export default OptimizeTest;
