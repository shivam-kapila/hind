import * as React from "react";

type CardProps = {
  className?: string;
  children: React.ReactNode;
  [key: string]: any;
};

const Card = React.forwardRef<HTMLDivElement, CardProps>(
  (props: CardProps, ref) => {
    const { children, className, ...cardProps } = props;

    return (
      <div {...cardProps} ref={ref} className={`card ${className}`}>
        <>{children}</>
      </div>
    );
  }
);

Card.defaultProps = {
  className: null,
};

export default Card;
